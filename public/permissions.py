from comments.permissions import get_registry, RootPerms, DetailPerms


class Root(RootPerms):
    def can_list_comments(self, request, content_type, object_pk):
        return True

    def can_create_comment(self, request, content_type, object_pk):
        return True


class Detail(DetailPerms):
    def can_get_comment(self, request, content_type, object_pk, comment_id):
        return True

    def can_update_comment(self, request, content_type, object_pk, comment_id):
        return True

    def can_delete_comment(self, request, content_type, object_pk, comment_id):
        return True


def init_permissions():
    registry = get_registry()
    registry.set_permissions(root=Root(), detail=Detail())