from typing import Any, Dict, List, Optional, Tuple, Union

from motor.motor_asyncio import AsyncIOMotorClient


class AsyncMongoDB:
    """
    Async Class for interacting with Bot database.
    """

    def __init__(
        self,
        database_url: str,
        database_name: Optional[str] = "test",
        collection: Optional[str] = "test",
    ) -> None:
        """
        Initialize the database.

        Args:
            database_url: The url of the database.
            database_name: The name of the database, defaults to "test".
            collection: The collection to use, defaults to "test".
        """
        self.db_client = AsyncIOMotorClient(database_url)
        self.main_db = self.db_client[database_name]
        self.collection = self.main_db[collection]

    async def insert_one(
        self,
        document: Dict[str, Any],
    ) -> Optional[str]:
        """
        Insert one document into collection.

        Args:
            document: The document to insert.

        Returns:
            The inserted_id of the inserted document.
        """
        result = await self.collection.insert_one(document)
        return repr(result.inserted_id)

    async def find_one(
        self,
        query: Dict[str, Any],
    ) -> Union[Dict[str, Any], None]:
        """
        Find one entry from collection.

        Args:
            query: The query to find the entry.

        Returns:
            The entry that matches the query.
        """
        result = await self.collection.find_one(query)
        return result if result else None

    async def find_all(
        self,
        query: Optional[Union[Dict[str, Any], None]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Find all entries from collection.

        Args:
            query: The query to find the entries.

        Returns:
            The list of entries that match the query.
        """
        if query is None:
            query = {}
        return [document async for document in self.collection.find(query)]

    async def count(self, query: Optional[Union[Dict[str, Any], None]] = None) -> int:
        """
        Count the number of entries in collection.

        Args:
            query: The query to count the entries.

        Returns:
            The number of entries that match the query.
        """
        if query is None:
            query = {}
        return await self.collection.count_documents(query)

    async def delete_one(
        self, query: Optional[Union[Dict[str, Any], None]]
    ) -> Tuple[int, int]:
        """
        Delete one entry from collection.

        Args:
            query: The query to delete the entry.

        Returns:
            The number of entries after deleting the query.
        """
        before_delete = await self.collection.count(query)
        await self.collection.delete_many(query)
        after_delete = await self.collection.count_documents({})
        return before_delete, after_delete

    async def replace(
        self,
        query: Dict[str, Any],
        new_data: Dict[str, Any],
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Replace one entry from collection.

        Args:
            query: The query to replace the entry.
            new_data: The new data to replace the entry with.

        Returns:
            The old data and the new data.
        """
        old = await self.collection.find_one(query)
        _id = old["_id"]
        await self.collection.replace_one({"_id": _id}, new_data)
        new = await self.collection.find_one({"_id": _id})
        return old, new

    async def update(
        self,
        query: Dict[str, Any],
        update: Dict[str, Any],
    ) -> Tuple[Union[int, str], Dict[str, Any]]:
        """
        Update one entry from collection.

        Args:
            query: The query to update the entry.
            update: The update to update the entry with.

        Returns:
            The number of entries after updating the query and the updated document.
        """
        result = await self.collection.update_one(query, {"$set": update})
        new_document = await self.collection.find_one(query)
        return result.modified_count, new_document

    async def db_command(
        self,
        command: str,
    ) -> Optional[str]:
        """
        Execute a database command.

        Args:
            command: The command to execute.

        Returns:
            The result of the command.
        """
        result = await self.main_db.command(command)
        return result
