from django.test import TestCase
from Course.models import Course
from Account.models import Account
from TACourse.AssignTACourse import AssignTACourse
from TACourse.models import TACourse


class TestAssignTACourse(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(userName="Tuvix", title="1")
        self.account2 = Account.objects.create(userName="Q", title="2")
        self.Course1 = Course.objects.create(number="535", name="AlgorithmDesignAndAnalysis")
        self.Course2 = Course.objects.create(number="351", name="DataStructuresAndAlgorithms")
        self.assign = AssignTACourse()

    def test_assignTACourse_tooFewArgs(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Neelix"]),
                         "Your command has an incorrect "
                         "number of arguments, please enter your command in the following format: "
                         "assignTACourse userName classNumber")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_tooManyArgs(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Neelix", "351", "344"]),
                         "Your command has an incorrect "
                         "number of arguments, please enter your command in the following format: "
                         "assignTACourse userName classNumber")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_accountNotFound(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Neelix", "535"]), "Invalid TA username.")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_courseNotFound(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Tuvix", "874"]), "Invalid course number.")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_already_exists(self):
        TACourse.objects.create(TA=self.account1, Course=self.Course1)

        self.assertEqual(self.assign.assignTACourse(["", "Tuvix", "535"]), "Tuvix is already assigned to AlgorithmDesignAndAnalysis")

    def test_assignTACourse_invalidTitle(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Q", "351"]), "Account is not a TA.")

    def test_assignTACourse_success(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Tuvix", "535"]), "Assignment successful.")

        self.assertTrue(TACourse.objects.exists())

        a = TACourse.objects.get()

        self.assertEqual(a.Course, Course.objects.get(number=535))

        self.assertEqual(a.TA, Account.objects.get(userName="Tuvix"))


