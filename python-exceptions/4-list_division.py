#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        dive_result = 0

        try:
            divid = my_list_1[i] / my_list_2[i]
            dive_result = divid

        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result.append(dive_result)

    return result
