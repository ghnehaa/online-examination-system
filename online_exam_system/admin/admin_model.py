"""
admin/admin_model.py — Admin entity class
"""


class Admin:
    def __init__(self, admin_id: str, name: str, password: str):
        self.admin_id = admin_id
        self.name = name
        self.password = password

    def __repr__(self):
        return f"Admin(id={self.admin_id}, name={self.name})"
