from pysnmp import hlapi
import datetime

def get(target, oids, credentials, port=161, engine = hlapi.SnmpEngine(),context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
        )
    return fetch(handler, 1)[0]

def get_bulk(target, oids, credentials, count, start_from=0, port = 161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.bulkCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        start_from, count,
        *construct_object_types(oids)
        )
    return fetch(handler, count)

def get_bulk_auto(target, oids, credentials, count_oid, start_from=0, port = 161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    count = get(target, [count_oid], credentials, port, engine, context)[count_oid]
    return get_bulk(target, oids, credentials, count, start_from, port, engine, context)

def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types

def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except(ValueError, TypeError):
            try:
                return str(value)
            except(ValueError, TypeError):
                pass
    return value
    
def get_time():
    up_time = get('10.10.1.1', ['1.3.6.1.2.1.1.3.0'], hlapi.CommunityData('ciscolab'))
    up_time = up_time.get('1.3.6.1.2.1.1.3.0')
    seconds = up_time/100
    td_str = str(datetime.timedelta(seconds=seconds))
    x = td_str.split(':')
    return x[0], 'Hours', x[1], 'Minutes', x[2].split('.', 2)[0], 'Seconds'

def get_int_bulk_result():
    its = get_bulk_auto(
        '10.10.1.1', ['1.3.6.1.2.1.2.2.1.8'],
        hlapi.CommunityData('ciscolab'), '1.3.6.1.2.1.2.1.0')


    for it in its:
            for k, v in it.items():
                if v == 1:
                    v = 'up'
                elif v == 2:
                    v = 'down'
                else:
                    v = 'unknown'

                print("{0} = {1}".format(k,v))

            print('')


#print(get('10.10.1.1', ['1.3.6.1.2.1.1.5.0'], hlapi.CommunityData('ciscolab')))
#print(get('10.10.1.1', ['1.3.6.1.2.1.3.1.1.1'], hlapi.CommunityData('ciscolab')))


#its = get_bulk('10.10.1.1', ['1.3.6.1.2.1.3.1.1.2'], hlapi.CommunityData('ciscolab'), 32)
#print(get_bulk('10.10.1.1', ['1.3.6.1.2.1.3.1.1.1'], hlapi.CommunityData('ciscolab'), 1))

#print(its)


#its = get_bulk_auto('10.10.1.1', ['1.3.6.1.2.1.3.1.1.3'], # '1.3.6.1.2.1.2.2.1.2' ,'1.3.6.1.2.1.31.1.1.1.18') hlapi.CommunityData('ciscolab'), '1.3.6.1.2.1.2.1.0')#1.3.6.1.2.1.2.1.0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    