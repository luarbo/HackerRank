	# Add your code here
    difference=0
    def computeDifference(self):
        self.maximumDifference=0
        for i in range (len(a)):
            for j in range (i+1, len(a)):
                difference = abs(a[i]-a[j])
                self.maximumDifference = max (difference, self.maximumDifference)
    
