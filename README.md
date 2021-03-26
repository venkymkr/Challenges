# KPMG
Three Challenges
Challenge 1: 
There are three layers in three tier architecture which are Presentation layer, Business logic layer and Data access layer. Apart from these three we can use a business object layer to implement property classes that can map our objects with the database or you can use entity framework.

Presentation layer : This is the top-most layer of the application where the user performs their activity. Let's take the example of any application where the user needs to fill up a form. This form is nothing but the Presentation Layer. In Windows applications Windows Forms are the Presentation Layer and in web applications the web form belongs to the Presentation Layer. Basically the user's input validation and rule processing is done in this layer.

Business layer : This is on top of the Presentation Layer. As the name suggests, most of the business operations are performed here. For example, after collecting form data we want to validate them with our custom business rule. Basically we define classes and business entities in this layer.

Data access layer : On top of the Business Logic Layer is the Data Access Layer. It contains methods that help the business layer to connect with the database and perform CRUD operations. Generally all database related code and stuff belongs to the Data Access Layer. Sometimes people use a platform-independent Data Access Layer to fetch data from various database vendors.

Source/Further details - https://www.c-sharpcorner.com/UploadFile/dacca2/understand-3-tier-architecture-in-C-Sharp-net/

Challenge 2 :
Code to Query Metadata of an Instance within AWS


Challenge 3 :
Tests
def test_get():
  assert get(None, ['foo']) == None
  assert get({'foo': 1}, None) == None
  assert get(None, None) == None
  assert get({'foo': 1}, []) == {'foo': 1}
  assert get({'foo': 1}, ['foo']) == 1
  assert get({'foo': 1}, ['bar']) == None
  assert get({'foo': 1}, ['bar'], 'the default') == 'the default'
  assert get({'foo': {'bar': 'hello'}}, ['foo', 'bar']) == 'hello'
  assert get({'foo': {'bar': 'hello'}}, 'foo.bar') == 'hello'
  assert get({'foo': [{'bar': 'hello'}]}, 'foo.0.bar') == 'hello'
  assert get({'foo': [{'bar': 'hello'}]}, 'foo.1') == None
  assert get({'foo': [{'bar': 'hello'}]}, 'foo.1.bar') == None
  assert get(['foo', 'bar'], '1') == 'bar'
  assert get(['foo', 'bar'], '2') == None
