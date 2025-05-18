class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner or None")

        self._owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, Owner):
            raise Exception("new_owner must be an instance of Owner")
        self._owner = new_owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self  # Assign this owner to the pet

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
