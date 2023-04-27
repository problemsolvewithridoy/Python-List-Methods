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
