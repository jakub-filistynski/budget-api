class ActionSerializerMixin:
    """
    Mixin umożliwia wybranie serializera w zależności od akcji/metody http.
    Przykład:
    action_serializer_classes = {
        'create': CreateSerializer,
        'post': ExamplePostSerializer,
        'custom_action': CustomActionSerializer,
    }
    """

    action_serializer_classes = {}

    def get_serializer_class(self):
        request_method_name = self.request.method.lower()
        if hasattr(self, "action"):
            return (self.action_serializers.get(self.action, self.serializer_class),)
        return self.action_serializers.get(request_method_name, self.serializer_class)
