class Pagination():
    def __init__(self, items=None, pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = self.calculate_total_pages()

    def calculate_total_pages(self):
        if self.items:
            return (len(self.items) + self.pageSize - 1) // self.pageSize
        return 0

    def getVisibleItems(self):
        if self.items is None:
            return []
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        self.currentPage = max(1, min(self.totalPages, int(pageNum)))
        return self


# checking
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
 # ["a", "b", "c", "d"]

p.nextPage()

print(p.getVisibleItems())
# ["e", "f", "g", "h"]

p.lastPage()

print(p.getVisibleItems())
# ["y", "z"]