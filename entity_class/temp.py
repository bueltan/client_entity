def callback_method(func):
    def notify(self,*args,**kwargs):
        for _,callback in self._callbacks:
            callback()
        return func(self,*args,**kwargs)
    return notify

class NotifyList(list):
    append = callback_method(list.append)
    def __getitem__(self,item):
        if isinstance(item,slice):
            return self.__class__(list.__getitem__(self,item))
        else:
            return list.__getitem__(self,item)

    def __init__(self,*args):
        list.__init__(self,*args)
        self._callbacks = []
        self._callback_cntr = 0

    def register_callback(self,cb):
        self._callbacks.append((self._callback_cntr,cb))
        self._callback_cntr += 1
        return self._callback_cntr - 1

class populateList():

    def __init__(self, **kwargs):
        list =  NotifyList(range(10))
        cbid = list.register_callback(self.cb)

        list.append('Foo')
        list.append('Foo')


    def cb(self):
        print ("Appen!")


    #register_class a callback


if __name__ == '__main__':

    populateList()