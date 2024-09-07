import graphene
from graphene_django.types import DjangoObjectType
from banks.models import Bank, Branch

class BankType(DjangoObjectType):
    class Meta:
        model = Bank

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch

class Query(graphene.ObjectType):
    all_banks = graphene.List(BankType)
    bank_branches = graphene.List(BranchType, bank_id=graphene.Int())

    def resolve_all_banks(self, info, **kwargs):
        return Bank.objects.all()

    def resolve_bank_branches(self, info, bank_id):
        return Branch.objects.filter(bank__id=bank_id)

schema = graphene.Schema(query=Query)
