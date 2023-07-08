
from django.utils import timezone
import datetime


def io_match(io_get, ios):
    match io_get:
        case 'day':
            ios = ios.filter(date__day = timezone.now().day)
        case 'week':
            ios = ios.filter(date__gte=timezone.now()-datetime.timedelta(days=7))
        case 'month':
            ios = ios.filter(date__month= timezone.now().month)
        case 'year':
            ios = ios.filter(date__year = timezone.now().year)
        case 'all':
            ios = ios  #não necessita de filtro

    return ios