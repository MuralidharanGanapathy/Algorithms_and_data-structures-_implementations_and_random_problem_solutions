#k-means clustering for 2-d datasets
def k_means(l1, l2):
    return (((l2[0] - l1[0]) ** 2 ) + ((l2[1] - l1[1]) ** 2)) ** (1/2)
def centroid_update(l1, l2):
    X = (l1[0]+l2[0])/2
    Y = (l1[1] + l2[1])/2
    l = []
    l.append(X)
    l.append(Y)
    return l
    
n = int(input(print("Enter the number of datasets")))
print("Enter the X nad Y co-ordinates <space seperated>")
datasets = []
for _ in range(n):
    datasets.append(list(map(int, input().split())))
number_of_clusters = int(input())
if len(datasets) <= number_of_clusters:
    print("Individual datapoints")
else:
    cluster_dict = {}
    centroids = []
    for i in range(number_of_clusters):
        cluster_dict[i+1] = i + 1
        centroids.append(datasets[i])

    for i in range(number_of_clusters, len(datasets)):
        l = []
        for iterator in range(len(centroids)):
            l.append(k_means(datasets[i], centroids[iterator]))
        
        cluster_dict[i + 1] = l.index(min(l)) + 1
        centroids[l.index(min(l))] = centroid_update(centroids[l.index(min(l))], datasets[i])
    
    print("The datasets, co-ordinates and assigned-clusters")
    for keys in cluster_dict.keys():
        print(keys, datasets[keys - 1], cluster_dict[keys])
    
    
