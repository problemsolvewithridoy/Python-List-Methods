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
