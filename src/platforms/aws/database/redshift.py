# -*- coding: utf-8 -*-
import redshift_connector
import polars as pl
import pandas as pd

from src.controllers.exceptions import AutoArtAPIError, InvalidConfigurationError, ConnectionNotFoundError

class Redshift:
    def __init__(self, configs:dict):
        self._configs = configs
        self._conn = None
        self._connect()

    def __del__(self):
        self._disconnect()

    def _connect(self):
        try:
            self._conn = redshift_connector.connect(
                                                    host=self._configs['host'],
                                                    database=self._configs['database'], 
                                                    port=int(self._configs['port']), 
                                                    user=self._configs['username'], 
                                                    password=self._configs['password']
                                                    )
        except KeyError as e:
            raise InvalidConfigurationError(f'One or more configuration keys are missing: {str(e)}')
        except Exception as e:
            raise AutoArtAPIError(f'Connection cannot be established to Redshift: {str(e)}')

    def _disconnect(self):
        if self._conn is not None:
            try:
                self._conn.close()
            except Exception as e:
                raise AutoArtAPIError(f'Connection cannot be closed in Redshift: {str(e)}')

    def read(self, sql_query:str) -> pl.DataFrame:
        """
        Execute the provided 'sql_query' to fetch data from Redshift.

        Parameters
        ----------
        sql_query:str
            The SQL query to be executed for retrieving data.

        Returns
        -------
        df:pl.DataFrame
            A dataframe containing the query results. The output is automatically converted
            from pd.DataFrame to pl.DataFrame.

        Raises
        ------
        ConnectionNotFoundError
            If the operation is tried to perform without connection.

        AutoArtAPIError
            Other issues that cause not to complete operation.

        Notes
        -----
        AutoArt recommends that developers ensure SQL queries passed to the 'read' function
        are either static or parameterized to prevent SQL injection vulnerabilities.
        """
        if self._conn is None:
            raise ConnectionNotFoundError('No active connection to perform read operation.')

        try:
            with self._conn.cursor() as cursor:
                cursor.execute(sql_query)
                df = cursor.fetch_dataframe()
        except Exception as e:
            raise AutoArtAPIError(f'Read operation from Redshift could not be done: {str(e)}')

        return pl.from_pandas(df)

    def write(self, df:pl.DataFrame, table_name:str) -> None:
        """
        Insert the provided dataframe into a specified Redshift table.

        Parameters
        ----------
        df:pl.DataFrame
            A dataframe containing the data to be inserted. The input is automatically converted
            from pd.DataFrame to pl.DataFrame.

        table_name:str
            The name of target Redshift table where data will be inserted.

        Raises
        ------
        ConnectionNotFoundError
            If the operation is tried to perform without connection.

        AutoArtAPIError
            Other issues that cause not to complete operation.
        """
        if self._conn is None:
            raise ConnectionNotFoundError('No active connection to perform write operation.')

        try:
            with self._conn.cursor() as cursor:
                cursor.write_dataframe(df.to_pandas(), table=table_name)
        except Exception as e:
            raise AutoArtAPIError(f'Write operation from Redshift could not be done: {str(e)}')
