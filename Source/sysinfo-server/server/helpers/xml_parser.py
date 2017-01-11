from xml.etree import ElementTree


def xml_to_list(file_path):
    """
    XML to List function to tranform a XML file into Python List Object
    :param file_path:string
    :return: xml_list:list
    """
    xml_list = []

    try:
        xml_tree = ElementTree.parse(file_path)
        xml_root = xml_tree.getroot()
        for client in xml_root.findall('client'):
            xml_list.append({
                'ip': client.get('ip'),
                'username': client.get('username'),
                'password': client.get('password'),
                'port': client.get('port'),
                'alerts': [{
                    'type': alert.get('type'),
                    'limit': alert.get('limit')
                } for alert in client.findall('alert')]
            })
    except IOError, e:
        print 'Error find the XML file \'%s\':' % file_path, e
    except ElementTree.ParseError, e:
        print 'Error to parse the XML file \'%s\':' % file_path, e
    except Exception, e:
        print 'Error read the XML file \'%s\':' % file_path, e
    finally:
        return xml_list

