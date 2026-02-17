class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
       for i in range(len(image)) :
            left = 0
            right = len(image[i])-1
            while(left<=right):
                image[i][left],image[i][right] = 1-image[i][right], 1-image[i][left]
                left+=1
                right-=1
       return image
