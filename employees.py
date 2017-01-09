class Company(object):
    """ Contains methods for finding an employees name, when they started, and job title
    Methods:
    -----------
    getName
    getTitle
    getStartDate
    """
    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def getName(self, name):
        return self.name

    # Add the remaining methods to fill the requirements above

    def getTitle(self, title):
        return self.title

    def getStartDate(self, date):
        return self.start_date

    def __str__(self):
        return '%s is the %s and they started %s' % (self.name, self.title, self.start_date)



employee = Company('john', 'manager', 1999)
print(employee.__doc__)
print(employee)