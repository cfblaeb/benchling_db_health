class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'backend':
            return 'benchling'
        return None

    #def db_for_write(self, model, **hints):
    #    """
    #    Attempts to write auth models go to auth_db.
    #    """
    #    if model._meta.app_label == 'auth':
    #        return 'auth_db'
    #    return None

    #def allow_relation(self, obj1, obj2, **hints):
    #    """
    #    Allow relations if a model in the auth app is involved.
    #    """
    #    if obj1._meta.app_label == 'auth' or \
    #       obj2._meta.app_label == 'auth':
    #       return True
    #    return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'benchling':
            return False
        return True
