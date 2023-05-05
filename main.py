from package import do_logging as do


class listfile:
    try:
        def __init__(self,l):
            self.l=l
            do.log("this data geven by user: %s ", self.l)

        def do_append(self,value):
            try:
                do.log("this is new data whcich append by user: %s ",value)
                self.l[len(self.l):len(self.l)] = [value]
                do.log("this is a final list after append data: %s ", self.l)


            except Exception as e:
                do.log_error("Error is happend")
                do.log_exception("error is: %s", str(e))

        def do_clear(self):
            try:
                del self.l[:]
                do.log("after use clear function data is: %s",self.l)
            except Exception as e:
                do.log_error("Error is happened")
                do.log_exception("error is %s", str(e))

        def do_copy(self):
            try:
                a = self.l[:]
                do.log("this is my new copy list data: %s", a)
            except Exception as e:
                do.log_error("Error is happend")
                do.log_exception("error is %s", str(e))

        def do_count(self,value):
            try:
                do.log("user want to know how much: %s is here", value)
                count = 0
                for i in self.l:
                    if i == value:
                        count += 1
                do.log("count result is: %s", count)

            except Exception as e:
                do.log_error("Error is Happend")
                do.log_exception("error is: %s", str(e))

        def do_extend(self,value):
            try:
                do.log("user want to extend: %s", value)
                self.l[len(self.l):len(self.l)] = value
                do.log("after extend data is: %s", self.l)

            except Exception as e:
                do.log_error("Error is Happend")
                do.log_exception("error is: %s", str(e))

        def do_index(self,value):
            try:
                do.log("user want to know %s value's index", value)
                count = 0
                if value in self.l:
                    for i in self.l:
                        count +=1
                        if i == value:
                            break
                else:
                    do.log("%s is not in list",value)
                if count == 0:
                    pass
                else:
                    do.log("Index number is %s",count-1)

            except Exception as e:
                do.log_error("Error is Happend")
                do.log_exception("error is: %s", str(e))

        def do_insert(self,index_point, value ): #(self,2,4)
            try:
                do.log("user give %s value", value)
                self.l[index_point:index_point] = [value]
                do.log("insert successful, %s value", value)
                do.log("after insert value list is: %s", self.l)

            except Exception as e:
                do.log_error("Error is Happend")
                do.log_exception("error is: %s", str(e))

        def do_pop(self, value=-1):
            try:
                do.log("user want to delete %s value",value)
                del self.l[value]
                do.log("value is deleted successfully & after delete list is: %s", self.l)
            except Exception as e:
                do.log_error("Error is happend")
                do.log_exception("error is %s",e)

        def do_remove(self,value):
            try:
                do.log("user want to delete %s value", value)
                if value in self.l:
                    for i in range(len(self.l)):
                        if self.l[i] == value:
                            del self.l[i]
                            break
                    do.log("after remove list is: %s", self.l)
                else:
                    raise Exception(f"{value} is not in list")

            except Exception as e:
                do.log_error("Error is happend")
                do.log_exception("error is %s", str(e))

        def do_reverse(self):
            try:
                do.log("this data give by user: %s and user want to reverse it ", self.l)
                l = self.l[::-1]
                do.log("after reverse list is %s", l)

            except Exception as e:
                do.log_error("Error is Happend")
                do.log_exception("error is %s", e)

        def do_sort(self,key = None, reverse = False ):
            try:
                if key != None:
                    l1 = []
                    l2 = []
                    l3 = []

                    for i in self.l:
                        a = len(i)
                        l1[len(l1):len(l1)] = [a]
                    for i in range(len(l1)):
                        a = min(l1)
                        l2[len(l2):len(l2)] = [a]
                        if a in l1:
                            for i in range(len(l1)):
                                if l1[i] == a:
                                    del l1[i]
                                    break
                    s = set(l2)
                    for i in s:
                        for j in self.l:
                            if i == len(j):
                                l3[len(l3):len(l3)] = [j]
                    self.l = l3
                    if reverse == True:
                        self.l = self.l[::-1]
                        do.log("this is your sort & reverse data: %s", self.l)
                    else:
                        do.log("this is your sort data: %s", self.l)
                else:

                    l1 = []
                    for i in range(len(self.l)):
                        a = min(self.l)
                        l1[len(l1):len(l1)] = [a]
                        self.l.remove(a)
                    self.l = l1
                    if reverse == True:
                        self.l = self.l[::-1]
                        do.log("this is your sort & reverse data: %s", self.l)
                    else:
                        do.log("this is your sort data: %s", self.l)
            except Exception as e:
                do.log_error("Error is Happend")
                do.log_exception("error is : %s", str(e))
