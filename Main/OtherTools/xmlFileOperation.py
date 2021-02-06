# 整理：cooper
# 来源: https://blog.csdn.net/wsp_1138886114/article/details/86576900
# 日期：2020-01-29

from xml.etree.ElementTree import ElementTree, Element


class XmlFile:
    def __init__(self):
        pass

    def read_xml(self, in_path):
        """
        读取并解析xml文件
        :param in_path: xml路径
        :return:ElementTree
        """
        element_tree = ElementTree()
        element_tree.parse(in_path)
        return element_tree

    def write_xml(self, tree, out_path):
        """
        导出xml文件至指定目录
        :param tree: xml树
        :param out_path: 写出路径
        :return:
        """

        tree.write(out_path, encoding="utf-8", xml_declaration=True)

    def if_match(self, node, kv_map):
        """
        判断某个节点是否包含所有传入参数属性
        :param node: 目标节点
        :param kv_map: 属性及属性值组成的map
        :return:
        """

        for key in kv_map:
            if node.get(key) != kv_map.get(key):
                return False
        return True


class XmlSearch(XmlFile):
    def find_nodes(self, root_tree, path):
        """
        查找某个路径匹配的所有节点
        :param root_tree: xml树
        :param path: 节点路径，从根目录下一级开始
        :return: 所有符合条件节点列表
        """
        return root_tree.findall(path)

    def get_node_by_key_value(self, nodelist, kv_map):
        """
        根据属性及属性值定位符合的节点，返回节点
        :param nodelist: 节点列表
        :param kv_map: 匹配属性及属性值map
        :return: 符合条件节点列表
        """

        result_nodes = []
        for node in nodelist:
            if self.if_match(node, kv_map):
                result_nodes.append(node)
        return result_nodes


class XmlChange(XmlFile):
    def change_node_properties(self, nodelist, kv_map, is_delete=False):
        """
        修改/增加 /删除 节点的属性及属性值
        :param nodelist: 节点列表
        :param kv_map: 属性及属性值map
        :param is_delete: 是否删除该节点属性
        :return:
        """

        for node in nodelist:
            for key in kv_map:
                if is_delete:
                    if key in node.attrib:
                        del node.attrib[key]
                else:
                    node.set(key, kv_map.get(key))

    def change_node_text(self, nodelist, text, is_add=False, is_delete=False):
        """
        改变/增加/删除一个节点的文本
        :param nodelist: 节点列表
        :param text: 更新后的文本
        :param is_add: 是否在原基础上追加
        :param is_delete: 是否删除
        :return:
        """

        for node in nodelist:
            if is_add:
                node.text += text
            elif is_delete:
                node.text = ""
            else:
                node.text = text

    def create_node(self, tag, property_map, content):
        """
        新造一个节点
        :param tag: 节点标签
        :param property_map: 属性及属性值map
        :param content: 节点闭合标签里的文本内容
        :return: 新节点
        """
        element = Element(tag, property_map)
        element.text = content
        return element

    def add_child_node(self, nodelist, element):
        """
        给一个节点添加子节点
        :param nodelist: 节点列表
        :param element: 子节点
        :return:
        """

        for node in nodelist:
            node.append(element)

    def del_node_by_tag_key_value(self, nodelist, tag, kv_map):
        """
        通过属性及属性值定位一个节点，并删除他
        :param nodelist: 父节点列表
        :param tag: 子节点标签
        :param kv_map: 属性及属性值列表
        :return:
        """
        for parent_node in nodelist:
            children = parent_node.getchildren()
            for child in children:
                if child.tag == tag and self.if_match(child, kv_map):
                    parent_node.remove(child)


if __name__ == "__main__":
    ################ 1. 读取xml文件  ##########
    xf = XmlFile()
    tree = xf.read_xml("test_02.xml")

    ################ 2. 属性修改 ###############
    xs = XmlSearch()
    xc = XmlChange()
    nodes = xs.find_nodes(tree, "processers/processer")  # 找到父节点
    result_nodes = xs.get_node_by_key_value(nodes, {"name": "BProcesser"})  # 通过属性准确定位子节点
    xc.change_node_properties(result_nodes, {"age": "1"})  # 修改节点属性
    xc.change_node_properties(result_nodes, {"value": ""}, True)  # 删除节点属性

    #################  3. 节点修改 ##############
    a = xc.create_node("person", {"age": "15", "money": "200000"}, "this is the firest content")  # 新建节点
    xc.add_child_node(result_nodes, a)  # 插入到父节点之下

    ################# 4. 删除节点 ################
    del_parent_nodes = xs.find_nodes(tree, "processers/services/service")  # 定位父节点
    target_del_node = xc.del_node_by_tag_key_value(del_parent_nodes, "chain", {"sequency": "chain1"})  # 准确定位子节点并删除之

    ################# 5. 修改节点文本 ############
    text_nodes = xs.get_node_by_key_value(xs.find_nodes(tree, "processers/services/service/chain"),
                                          {"sequency": "chain3"})  # 定位节点
    xc.change_node_text(text_nodes, "new text")

    ############## 6. 输出到结果文件  ##########
    xf.write_xml(tree, "./xiugai.xml")
