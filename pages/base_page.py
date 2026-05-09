import allure


class BasePage:
    """Base class that automatically wraps all public methods with allure.step()"""

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for name, val in list(cls.__dict__.items()):
            if (
                callable(val)
                and not name.startswith("_")
                and not isinstance(val, (staticmethod, classmethod))
            ):
                setattr(cls, name, allure.step(val))
