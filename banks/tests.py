from django.test import TestCase
# from banks.models import Bank, Branch
# from graphene.test import Client
# from bankapi.schema import schema

# class BankModelTest(TestCase):
#     def setUp(self):
#         # Create a Bank object
#         self.bank = Bank.objects.create(name="Test Bank")

#     def test_bank_creation(self):
#         # Test Bank creation
#         self.assertEqual(self.bank.name, "Test Bank")

#     def test_branch_creation(self):
#         # Create a Branch object associated with the Bank
#         branch = Branch.objects.create(
#             ifsc="TEST0000001", 
#             bank=self.bank,  # Associate with the Bank
#             branch="Main", 
#             address="123 Main St", 
#             city="Test City", 
#             district="Test District", 
#             state="Test State"
#         )
#         # Test Branch creation
#         self.assertEqual(branch.ifsc, "TEST0000001")
#         self.assertEqual(branch.bank.name, "Test Bank")

# class GraphQLTest(TestCase):
#     def setUp(self):
#         # Create a Bank object
#         self.bank = Bank.objects.create(name="Test Bank")
#         # Create a Branch object associated with the Bank
#         Branch.objects.create(
#             ifsc="TEST0000001", 
#             bank=self.bank,  # Associate with the Bank
#             branch="Main", 
#             address="123 Main St", 
#             city="Test City", 
#             district="Test District", 
#             state="Test State"
#         )
#         # Initialize GraphQL client
#         self.client = Client(schema)

#     def test_all_banks_query(self):
#         query = '''
#         {
#             allBanks {
#                 id
#                 name
#             }
#         }
#         '''
#         executed = self.client.execute(query)
#         # Validate the response
#         self.assertEqual(executed['data']['allBanks'][0]['name'], 'Test Bank')

#     def test_bank_branches_query(self):
#         query = '''
#         {
#             bankBranches(bankId: 1) {
#                 branch
#                 city
#             }
#         }
#         '''
#         executed = self.client.execute(query)
#         # Validate the response
#         self.assertEqual(executed['data']['bankBranches'][0]['branch'], 'Main')
#         self.assertEqual(executed['data']['bankBranches'][0]['city'], 'Test City')
