from linked_lists.linked_list import LinkedList

new_list = LinkedList()

if __name__ == '__main__':

    new_list.insert_at_end(55)
    new_list.insert_at_end(66)
    new_list.insert_at_end('end')
    new_list.insert_at_head('start')
    new_list.insert_at_head('start3')
    new_list.delete_at_head()
    print(new_list.is_empty())
    new_list.show()
    print(new_list)
    new_list.search('end')
    new_list.search('anf')
    new_list.delete(66)
    new_list.show()
    new_list.delete('start')
    new_list.delete('55')
    new_list.delete('end')
    new_list.show()
    print(new_list.is_empty())