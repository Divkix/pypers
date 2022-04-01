from functools import reduce
from types import SimpleNamespace
from typing import Any, Dict, List, Tuple


class Namespace(SimpleNamespace):
    """
    A nested namespace class that allows for nested dictionaries to be converted to a nested namespace.
    """

    def __init__(
        self,
        dictionary: Dict[str, Any] = None,
        **kwargs,
    ) -> None:
        """
        Initialize the namespace with a dictionary.

        Args:
            dictionary: The dictionary to initialize the namespace with.
            kwargs: Any additional keyword arguments to pass to the namespace.
        """
        if dictionary is None:
            dictionary = {}
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, list):
                self.__dict__[key] = [Namespace(item) for item in value]
            elif isinstance(value, dict):
                self.__setattr__(key, Namespace(value))
            else:
                self.__setattr__(key, value)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the namespace to a dictionary.

        Returns:
            The namespace as a dictionary.
        """
        for key, value in self.__dict__.items():
            if isinstance(value, Namespace):
                self.__dict__[key] = value.to_dict()
        return self.__dict__

    def keys(self) -> List[str]:
        """
        Get all top level keys of dictionary.

        Returns:
            The top level keys of the namespace.
        """
        return list(self.__dict__.keys())

    def items(self) -> Tuple[str, Any]:
        """
        Get all items of dictionary.

        Returns:
            The items of the namespace.
        """
        return self.__dict__.items()

    def rsetattr(self, attr: str, val: Any) -> None:
        """
        Set nested attribute of a nested namespace.

        Args:
            attr: The attribute to set.
            val: The value to set the attribute to.
        """
        pre, _, post = attr.rpartition(".")
        return setattr(self.rgetattr(pre) if pre else self, post, val)

    def rgetattr(self, attr: str, *args) -> Any:
        """
        Get nested attribute of a nested namespace.

        Args:
            attr: The attribute to get.
            args: Any additional arguments to pass to the getattr function.

        Returns:
            The value of the attribute.
        """

        def _getattr(obj: dict, attr: str) -> Any:
            return getattr(Namespace(obj), attr, *args)

        return reduce(_getattr, [self] + attr.split("."))

    def __iter__(self) -> List[Any]:
        """
        Enables iteration in class.

        Return:
            The items of the namespace.
        """
        return iter(self.__dict__)
