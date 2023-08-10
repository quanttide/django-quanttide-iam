from django_tenants.test.cases import TenantTestCase

from users.models import User
from organizations.models import Organization, OrganizationOwner, OrganizationMember


class OrganizationViewSetTestCase(TenantTestCase):
    def setUp(self):
        """
        TODO: 通过fixture导入样例数据。
        """
        # 用户
        self.user1 = User.objects.create()
        self.user2 = User.objects.create()
        self.user3 = User.objects.create()
        # 组织
        self.org_a = Organization.objects.create(name='org-a', verbose_name='组织A')
        self.org_b = Organization.objects.create(name='org-b', verbose_name='组织B')
        # 组织成员
        self.org_member_a1 = OrganizationMember.objects.create(organization=self.org_a, user=self.user1)
        self.org_member_a2 = OrganizationMember.objects.create(organization=self.org_a, user=self.user2)
        self.org_member_b2 = OrganizationMember.objects.create(organization=self.org_b, user=self.user2)
        self.org_member_b3 = OrganizationMember.objects.create(organization=self.org_b, user=self.user3)
        # 组织所有者
        self.org_owner_a1 = OrganizationOwner.objects.create(organization=self.org_a, member=self.org_member_a1)
        self.org_owner_b2 = OrganizationOwner.objects.create(organization=self.org_b, member=self.org_member_b2)

