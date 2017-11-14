from app.models import School
from app.managers import SecondarySchoolManager, MixedSchoolManager
from django.db.models import Q


class SecondarySchoolProxy(School):
    objects = SecondarySchoolManager()

    def get_schools_satisfy_psle(self, score):
        queryset = self.objects.all()
        queryset.filter(
           (Q(express_nonaff_lower__isnull=False) & Q(express_nonaff_lower__lte=score)) |
           (Q(normal_technical_nonaff_lower__isnull=False) & Q(normal_technical_nonaff_lower__lte=score)) |
           (Q(normal_academic_nonaff_lower__isnull=False) & Q(normal_academic_nonaff_lower__lte=score))
        )
        return queryset

    class Meta:
        proxy = True


class MixedSchoolProxy(School):
    objects = MixedSchoolManager()

    class Meta:
        proxy = True
