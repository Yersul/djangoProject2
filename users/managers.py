from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone, password, is_staff, is_superuser, **extra_fields):
        if not phone:
            raise ValueError('User must have phone number!')

        user = self.model(
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None,  **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('not found is_staff value')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('not found is_superuser value')
        return self._create_user(phone, password, **extra_fields)
