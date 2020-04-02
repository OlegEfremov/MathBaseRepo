# Декораторы для проверки прав доступа
#
# @user_passes_test(editor_check)
# def main_page():
#

from apps.Main.models import Solution_Folder


# Возвращает корневой каталог дерева решений
def sol_tree_root(folder_id):
    sol_folder = Solution_Folder.objects.get(id=folder_id)
    while sol_folder.parent is not None:
        sol_folder = Solution_Folder.objects.get(id=sol_folder.parent)

    return sol_folder


# Проверка доступа к операциям с каталогом решений
def sol_folder_check(user, folder_id):
    root = sol_tree_root(folder_id)

    if root.system_name == 'SYSTEM_ROOT_CATALOG':
        return admin_check(user)
    elif root.system_name == 'ROOT_CATALOG':
        if root.author == user:
            return reader_check(user)
        else:
            return superuser_check(user)

    return False


# Проверочная функция декоратора @user_passes_test для Editor
def editor_check(user):
    if not user.is_authenticated:
        return False
    if admin_check(user):
        return True
    return user.groups.filter(name="Editors").exists()


# Проверочная функция декоратора @user_passes_test для Reader
def reader_check(user):
    if not user.is_authenticated:
        return False
    if admin_check(user):
        return True
    return user.groups.filter(name__in=("Readers", "Editors", "Freinds")).exists()


# Проверочная функция декоратора @user_passes_test для Admin
def admin_check(user):
    if not user.is_authenticated:
        return False
    return user.groups.filter(name__in=("Admins", "Superusers")).exists()


# Проверочная функция декоратора @user_passes_test для Friends
def friends_check(user):
    if not user.is_authenticated:
        return False
    if admin_check(user):
        return True
    return user.groups.filter(name="Freinds").exists()


# Проверочная функция декоратора @user_passes_test для Superuser
def superuser_check(user):
    if not user.is_authenticated:
        return False
    return user.is_superuser
