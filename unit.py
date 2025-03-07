class UnitCounter:
    def __init__(self):
        # Dictionary to store units and their counts
        self.units = {}

    def add_unit(self, unit_name, count=1):
        """Add units to the counter."""
        if unit_name in self.units:
            self.units[unit_name] += count
        else:
            self.units[unit_name] = count
        print(f"Added {count} {unit_name}(s). Total: {self.units[unit_name]}")

    def remove_unit(self, unit_name, count=1):
        """Remove units from the counter."""
        if unit_name in self.units and self.units[unit_name] >= count:
            self.units[unit_name] -= count
            print(f"Removed {count} {unit_name}(s). Remaining: {self.units[unit_name]}")
            if self.units[unit_name] == 0:
                del self.units[unit_name]  # Remove the unit if count reaches zero
        else:
            print(f"Cannot remove {count} {unit_name}(s). Not enough in stock or unit doesn't exist.")

    def get_unit_count(self, unit_name):
        """Get the count of a specific unit."""
        return self.units.get(unit_name, 0)

    def list_all_units(self):
        """List all units and their counts."""
        if not self.units:
            print("No units in the counter.")
        else:
            for unit, count in self.units.items():
                print(f"{unit}: {count}")

# Example usage
if __name__ == "__main__":
    counter = UnitCounter()

    counter.add_unit("widget", 5)
    counter.add_unit("gizmo", 3)
    counter.remove_unit("widget", 2)
    print(f"Widget count: {counter.get_unit_count('widget')}")
    counter.list_all_units()
