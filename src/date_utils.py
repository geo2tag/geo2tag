from datetime import datetime
import json

ISO_FORMAT_ERROR = 'Error: not iso8601 format. Example: 2005-08-09T18:31:42.201000'
DATE_FIELD = 'date'

ISO8601_FMT_MILLS = '%Y-%m-%dT%H:%M:%S.%f'


def dateSerialiser(obj):
    if isinstance(obj, datetime):
        return '{0}{1}'.format(obj.isoformat(), '' if obj.microsecond > 0 else '.000000')
    raise TypeError('Type is not datetime')


def dateDeserialiser(dict_with_date, param_date):
    try:
        if param_date in dict_with_date and dict_with_date[param_date] is not None:
            obj = dict_with_date[param_date].replace('\'', "").replace('"', '')
            return datetime.strptime(obj, ISO8601_FMT_MILLS)
    except ValueError:
        print ISO_FORMAT_ERROR
        raise
    return None


def datetime_from_iso8601(datetime_str):
    return json.dumps(
        dateDeserialiser({DATE_FIELD: datetime_str}, DATE_FIELD),
        default=dateSerialiser)

