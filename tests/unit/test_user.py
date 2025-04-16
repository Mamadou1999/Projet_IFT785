from services.user import User

def test_user_authentication(user_data):
    """
        Vérifier que la méthode d'authentification fonctionne correctement
    """
    user = User()
    user.email = user_data["email"]
    user.password = user_data["password"]

    assert user.authenticate("test@example.com", "password_123") is True
    assert user.authenticate("test@example.com", "wrong_password") is False
    assert user.authenticate("wrong@example.com", "password_123") is False

def test_user_update_profile(user_data):
    """
        Vérifier que la mise à jour du profil fonctionne
    """
    user = User()
    user.email = user_data["email"]
    user.password = user_data["password"]

    user.update_profile({"email": "nouveau_mail@example.com"})
    assert user.email == "nouveau_mail@example.com"