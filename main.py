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
