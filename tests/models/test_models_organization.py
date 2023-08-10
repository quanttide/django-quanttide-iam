from django_tenants.test.cases import TenantTestCase

from users.models import User
from organizations.models import Organization, OrganizationOwner, OrganizationMember


class OrganizationTestCase(TenantTestCase):
    def test_init(self):
        org = Organization.objects.create(name='quanttide', verbose_name='量潮科技')


class OrganizationMemberManagerTestCase(TenantTestCase):
    def setUp(self):
        self.user1 = User.objects.create()
        self.user2 = User.objects.create()
        self.user3 = User.objects.create()
        self.org_a = Organization.objects.create(name='org-a')
        self.org_b = Organization.objects.create(name='org-b')

    def test_create(self):
        org_member_a1 = OrganizationMember.objects.create(organization=self.org_a, user=self.user1)
        org_member_a2 = OrganizationMember.objects.create(organization=self.org_a, user=self.user2)
        org_member_b2 = OrganizationMember.objects.create(organization=self.org_b, user=self.user2)
        org_member_b3 = OrganizationMember.objects.create(organization=self.org_b, user=self.user3)
        self.assertTrue(OrganizationMember.objects.filter(organization=self.org_a).exists())
        self.assertTrue(OrganizationMember.objects.filter(organization=self.org_b).exists())


class OrganizationOwnerMangerTestCase(TenantTestCase):
    def setUp(self):
        # 用户
        self.user1 = User.objects.create()
        self.user2 = User.objects.create()
        self.user3 = User.objects.create()
        # 组织
        self.org_a = Organization.objects.create(name='org-a')
        self.org_b = Organization.objects.create(name='org-b')
        # 组织成员
        self.org_member_a1 = OrganizationMember.objects.create(organization=self.org_a, user=self.user1)
        self.org_member_a2 = OrganizationMember.objects.create(organization=self.org_a, user=self.user2)
        self.org_member_b2 = OrganizationMember.objects.create(organization=self.org_b, user=self.user2)
        self.org_member_b3 = OrganizationMember.objects.create(organization=self.org_b, user=self.user3)

    def test_create(self):
        org_owner_a1 = OrganizationOwner.objects.create(organization=self.org_a, member=self.org_member_a1)
        org_owner_b2 = OrganizationOwner.objects.create(organization=self.org_b, member=self.org_member_b2)
        self.assertEqual(1, OrganizationOwner.objects.filter(organization=self.org_a).count())
        self.assertEqual(1, OrganizationOwner.objects.filter(organization=self.org_b).count())

    def test_create_multi_owners(self):
        """
        TODO: 创建多个所有者时会抛出异常，请开发者定义并在单元测试验证异常。
        """
        pass
