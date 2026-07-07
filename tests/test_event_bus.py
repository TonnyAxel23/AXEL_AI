from app.core.services.event_bus import EventBus

bus = EventBus()


def greet(name):
    print(f"Hello {name}")


bus.subscribe("user.login", greet)

bus.publish("user.login", "Tonny")