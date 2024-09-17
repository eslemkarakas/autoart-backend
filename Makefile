APP_VERSION = v0.1.0
REGION_NAME = eu-central-1
ECR_URI = 767397854793.dkr.ecr.eu-central-1.amazonaws.com
ECS_CLUSTER = autoart

# mlflow variables
ECR_REPOSITORY_MLFLOW = autoart-mlflow
ECS_SERVICE_MLFLOW = UNKNOWN
TASK_ID_MLFLOW = UNKNOWN
TD_ARN_MLFLOW = UNKNOWN
DOCKERFILE_PATH_MLFLOW = builder/Dockerfile.mlflow

# backend variables
ECR_REPOSITORY_BACKEND = autoart-backend
ECS_SERVICE_BACKEND = UNKNOWN
TASK_ID_MLFLOW = UNKNOWN
TD_ARN_BACKEND = UNKNOWN
DOCKERFILE_PATH_BACKEND = builder/Dockerfile.backend

# build image
build-docker-mlflow:
	DOCKER_BUILDKIT=1 docker build -f ${DOCKERFILE_PATH_MLFLOW} -t ${ECR_REPOSITORY_MLFLOW}:${APP_VERSION} .

build-docker-backend:
	DOCKER_BUILDKIT=1 docker build -f ${DOCKERFILE_PATH_BACKEND} -t ${ECR_REPOSITORY_BACKEND}:${APP_VERSION} .

# push image
push-docker-mlflow: build-docker-mlflow
	docker tag ${ECR_REPOSITORY_MLFLOW}:${APP_VERSION}  ${ECR_URI}/${ECR_REPOSITORY_MLFLOW}:latest
	docker push ${ECR_URI}/${ECR_REPOSITORY_MLFLOW}:latest

push-docker-backend: build-docker-backend
	docker tag ${ECR_REPOSITORY_BACKEND}:${APP_VERSION}  ${ECR_URI}/${ECR_REPOSITORY_BACKEND}:latest
	docker push ${ECR_URI}/${ECR_REPOSITORY_BACKEND}:latest

# update service
update-service-mlflow: push-docker-mlflow
	aws ecs update-service --cluster ${ECS_CLUSTER} --service ${ECS_SERVICE_MLFLOW} --task-definition ${TD_ARN_MLFLOW}

update-service-backend: push-docker-backend
	aws ecs update-service --cluster ${ECS_CLUSTER} --service ${ECS_SERVICE_BACKEND} --task-definition ${TD_ARN_BACKEND}

# stop task
stop-service-mlflow:
	aws ecs stop-service --cluster ${ECS_CLUSTER} --task ${TASK_ID_MLFLOW}

stop-service-backend:
	aws ecs update-service --cluster ${ECS_CLUSTER} --task ${TASK_ID_BACKEND}

# COMMANDS #
# !: provide continuous availability by stoping previous service after updating service
ecr-login:
	aws ecr get-login-password --region ${REGION_NAME} | docker login --username AWS --password-stdin ${ECR_URI}

deploy-mlflow:
	update-service-mlflow
	stop-service-mlflow

deploy-backend: 
	update-service-backend 
	stop-service-backend
