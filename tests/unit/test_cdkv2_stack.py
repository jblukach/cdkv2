import aws_cdk as core
import aws_cdk.assertions as assertions

from cdkv2.cdkv2_stack import Cdkv2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdkv2/cdkv2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Cdkv2Stack(app, "cdkv2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
