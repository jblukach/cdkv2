# bootstrap

```
npm install -g aws-cdk
export CDK_NEW_BOOTSTRAP=1 && cdk bootstrap --show-template > bootstrap/template.yaml
mkdir -p temp/cdkv2
cd temp/cdkv2
cdk init app --language python
cd ../..
cdk version
```

```
pip3 install -r requirements.txt --upgrade
cdk deploy --profile 4n6ir --all --require-approval never
cdk destroy --profile 4n6ir --all --force
```

https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html#bootstrapping-contract
