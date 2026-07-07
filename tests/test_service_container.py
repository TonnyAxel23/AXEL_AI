from app.core.services.service_container import ServiceContainer


class Logger:
    pass


class Database:
    pass


container = ServiceContainer()

container.register("logger", Logger())
container.register("database", Database())

logger = container.get("logger")
database = container.get("database")

print(type(logger).__name__)
print(type(database).__name__)

try:
    container.get("speech")
except KeyError as e:
    print(e)