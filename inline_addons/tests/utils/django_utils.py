

def create_superuser():
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
    except ImportError:
        from django.contrib.auth.models import User  # NOQA
    superuser = User.objects.create_superuser('admin',
                                              'admin@free.fr',
                                              'secret')
    return superuser
