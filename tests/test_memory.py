from app.memory.memory_manager import MemoryManager

memory = MemoryManager()

memory.remember(
    "name",
    "Tonny"
)

memory.remember(
    "github",
    "TonnyAxel23"
)

print(
    memory.recall("name")
)

item = memory.get_memory_item(
    "github"
)

print(item.id)

print(item.created_at)