---
aliases: 
tags: 
title: drf.最佳实践
date created: 星期六, 七月 1日 2023, 9:48:21 上午
date modified: 星期六, 七月 1日 2023, 10:11:15 上午
---

# drf.最佳实践

## 1. ViewSets

viewsets 的好处是使得你的代码保持一致，并且免于重复。如果你编写的 views 不止去做一件事，那么 viewsets 就是你想要的东西。

举例来说，如果你有一个 model 叫做 Tag，你需要列表、创建和详情的功能，你可以定义一个 viewset:

```python
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

class TagViewSet(mixins.ListModelMixin, 
                 mixins.CreateModelMixin, 
                 mixins.RetrieveModelMixin,
                 GenericViewSet): 
""" The following endpoints are fully provided by mixins: * List view * Create view """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)
```

viewset 的 mixins 可以被自由组合，你可以定义自己的 mixins 或者使用 ModelViewSet。

ModelViewset 可以为你提供以下方法：`.list()，.retrieve(), .create(), .update(), .partial_update(), .destroy()` 。

此外，当你使用 viewsets 时，也会令你的路由配置更加的清晰。

```python
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

api_router = DefaultRouter()
api_router.register(r'tag', TagViewSet, 'tag')

urlpatterns = [ url(r'^v1/', include(api_router.urls, namespace='v1')) ]
```

现在，你的 viewset 可以帮你实现以下功能：

- 获取 Tag 列表，发送 GET 请求给 `v1/tag/`
- 创建 Tag，发送 POST 请求给 `v1/tag/`
- 获取特定 Tag，发送 GET 请求给 `v1/tag/<tag_id>`

你甚至可以在 viewset 里面通过 `@action` 装饰器添加一些自定义的路由。

## 2. 理解不同类型的 serializers

作为一个 DRF 的使用者，你不必太去关心 views 或者路由配置，所以你可能会把绝大部分精力放在 serializers 上来。

serializers 是充当 Django 的 model 及其表现形式（例如 json）之间的翻译器。每一个 serializer 能够既被用作读也可用作写，初始化的方式决定了它将执行的动作。我们可以区分出三种不同类型的 serializer: `create, update, retrieve`。

如果你想要在序列化器外部传输数据，下面是一个例子：

```python
def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = ProfileSerializer(instance=instance)
    return Response(serializer.data)
```

但是创建时，你需要另一种写法：

```python
def create(self, request, *args, **kwargs):
    serializer = ProfileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
```

最后，当你更新一个实例，你不但要提供 instance，也要提供 data:

```python
def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = ProfileSerializer( instance=instance, data=request.data )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
```

`serializer.save()` 会基于初始化时的参数传递调用适当的内部方法。

## 3. 使用 SerializerMethodField

SerializerMethodField 是一个只读的字段，通过在其附加到的 serializer classs 上调用相应的方法，在请求处理时计算其值。

举例来说，你有一个 model，里面有一个字段 datetime 存储的是 models.DateTimeField 类型，但是你想在序列化时，获得 timestamp 类型的数据：

```python
from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    
    class Meta:
        model = Tag
        fields = ('label', 'created')
    
    def get_created(self, obj):
        return round(obj.created.timestamp())
```

`SerializerMethodField` 接收 `method_name`，但是通常使用默认的命名方法会更为便捷，比如 `get_<field_name>`。另外你要确保，不会为任何繁重的操作增加方法字段的负担。

## 4. 使用 source 参数

很多情况下，你的 model 里面定义的字段，与你想要序列化的字段不一样。你可以使用 source 参数，轻松解决这个问题。

举个例子：

```python
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    job_type = serializers.CharField(source='task_type')
    
    class Meta:
        model = Task
        fields = ('job_type',)
```

模型中的 `task_type` 会被转换成 `job_type`。这个操作不光适用于读，还适用于写。

另外，你还可以借助点语法去从关联的模型中获取字段。

```python
owner_email = serializers.CharField(source='owner.email')
```

## 5. 序列化字段的验证

除了在初始化 serializer 字段和 `serializer.validate（）`hook 可以传递的 `validators` 参数之外，此外还有一种字段级别的验证，可以帮你为单独的每个字段定义它们自己的验证方法。

我发现它有用的原因有两个：首先，它可以对特别的字段进行校验，进行解耦。其次，它可以产生结构化的错误响应。

这种验证方式的使用，和 `SerializerMethodField` 特别相似，只是这时候的函数名字形如 `def validate_<field_name>`。举个例子：

```python
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    bid = serializers.IntegerField()
    
    def validate_bid(self, bid: int) -> int:
        if bid > self.context['request'].user.available_balance:
            raise serializers.ValidationError(
             _('Bid is greater than your balance')
            )
        return bid
```

``

如果验证错误，会得到下面这样的输出：

```json
{ "bid": ["Bid is greater than your balance"] }
```

验证方法必须要返回一个值，之后会传给 model 实例。

另外要记住，字段级别的验证将会在 `serializer.validate()` 之前被 `serializer.to_internal_value()` 调用。

## 6. 把值直接传给 save 方法

某些情况下，将值从序列化器外部直接传递到其 save（）方法很方便。

此方法将采用可以等同于序列化对象的参数。以这种方式传递的值将不会得到验证。它可用于强制覆盖初始数据。

```python
serializer = EmailSerializer(data=request.data)
serializer.is_valid(raise_exception=True)
serializer.save(owner_id=request.user.id)
```

## 7. 使用 CurrentUserDefault

如果需要设置用户，比上面的例子更好的是，使用 `CurrentUserDefault`，这时候不必去重写 view 了。

```python
from rest_framework import serializers

class EmailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField( default=serializers.CurrentUserDefault() )
```

这将会做两件事。首先，将在请求对象中认证的用户设置为默认用户。其次，因为使用了 `HiddenField`，因此不会考虑任何传入的数据，所以不可能会设置成别的用户。

## 8. serializers 的初始数据

有时候你需要去获取 serializer 的最原始的数据。这是因为数据已经通过运行 `serializer.is_valid（）` 进行了修改，或者需要在 validated_data 尚不可用时比较验证方法中另一个字段的值。

数据能够通过 `serializer.initial_data` 被获取到，格式是 dict，举个例子：

```python
from rest_framework import serializers

class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    
    def validate_password1(self, password1):
        if password1 != self.initial_data['password2']:
            raise serializers.ValidationError( 'Passwords do not match' )
```

## 9. 在嵌套序列化程序中处理多个创建/更新/删除

大多数时候，序列化器是完全简单的，并且有一定的经验，没有什么可能出错。但是，有一些限制。当您必须在一个高级序列化程序中支持嵌套序列化程序中的多个创建，更新和删除操作时，事情可能会有些棘手。

这需要权衡：要选择处理较多的请求数量，还是在一个请求里处理较长的时间。

默认情况下，DRF 根本不支持多个更新。很难想象它如何支持所有可能的嵌套插入和删除类型。这就是 DRF 的创建者选择灵活性而非现成的“万能”解决方案的原因，并把特权留给了我们。

在这种情况下，可以遵循两种路径：

- 使用颇受欢迎的第三方库 DRF Writable Nested
- 自己做

我建议至少选择一次第二个选项，这样您就会知道其中的含义。

在分析传入数据之后，在大多数情况下，我们可以做出以下假设：

- 所有应更新的实例都有 ID，
- 所有应创建的实例都没有 ID，
- 所有应删除的实例都都存在于数据存储（例如数据库）中，但不会出现在传入的 request.data 中。

基于此，我们知道如何处理列表中的特定实例。以下是详细显示此过程的代码段：

```python
class CUDNestedMixin(object):
    @staticmethod
    def cud_nested(queryset: QuerySet, data: List[Dict], serializer: Type[Serializer], context: Dict):
    """ Logic for handling multiple updates, creates and deletes on nested resources.
    :param queryset: queryset for objects existing in DB
    :param data: initial data to validate passed from higher level serializer to nested serializer
    :param serializer: nested serializer to use
    :param context: context passed from higher level serializer
    :return: N/A """
    updated_ids = list() 
    for_create = list() 
    for item in data: 
        item_id = item.get('id') 
        if item_id: instance = queryset.get(id=item_id) 
            update_serializer = serializer( instance=instance, data=item, context=context ) 
            update_serializer.is_valid(raise_exception=True) 
            update_serializer.save() 
            updated_ids.append(instance.id)
        else: 
            for_create.append(item)
            delete_queryset = queryset.exclude(id__in=updated_ids)
            delete_queryset.delete()
        
        create_serializer = serializer( data=for_create, many=True, context=context ) 
        create_serializer.is_valid(raise_exception=True) 
        create_serializer.save()
```

这是高级序列化程序如何利用此 mixin 的简化版本：

```python
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer, CUDNestedMixin): 
    phone_numbers = PhoneSerializer( many=True, source='phone_set', ) 
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_numbers') 
    
    def update(self, instance, validated_data):
        self.cud_nested(queryset=instance.phone_set.all(), 
                        data=self.initial_data['phone_numbers'],
                        serializer=PhoneSerializer, context=self.context
            )
        ...
        return instance
```

请记住，嵌套对象应使用 `initial_data` 而不是 `validated_data`。

那是因为运行验证会在序列化器的每个字段上调用 `field.to_internal_value（）`，这可能会修改特定字段存储的数据（例如，通过将主键更改为模型实例）。

## 10. 覆盖数据以强制排序

通过在 view 上的 queryset 添加排序，可以轻松地实现对列表视图的排序，但是在还应该对嵌套资源进行排序的情况下，并不是那么简单。

对于只读字段，可以在 `SerializerMethodField` 中完成，但是在必须写字段的情况下该怎么办？

在这种情况下，可以覆盖序列化程序的 `data` 属性，如以下示例所示：

```python
@property
def data(self):
    data = super().data
    data['phone_numbers'].sort(key=lambda p: p['id'])
    return data
```
