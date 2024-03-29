import numpy as np


class StochasticBlockModel:

    def __init__(self, p_in_pos, p_in_neg, p_out_pos, p_out_neg, num_clusters, cluster_size):
        self.p_in_pos = p_in_pos
        self.p_in_neg = p_in_neg
        self.p_out_pos = p_out_pos
        self.p_out_neg =  p_out_neg
        self.num_clusters = num_clusters
        self.cluster_size = cluster_size

    def same_cluster(self, i, j):
        return i/self.cluster_size == j/self.cluster_size

    def cluster_assignmnet(self, i):
        return i/self.cluster_size

    def generate_signed_graph(self):

        num_vertices = self.num_clusters * self.cluster_size

        positive_weight_matrix = np.zeros((num_vertices, num_vertices))
        negative_weight_matrix = np.zeros((num_vertices, num_vertices))

        for i in range(num_vertices):
            for j in range(i, num_vertices):
                if self.same_cluster(i, j):
                    positive_weight_matrix[i][j] = np.random.choice([1, 0], p=[self.p_in_pos, 1 - self.p_in_pos])
                    negative_weight_matrix[i][j] = np.random.choice([1, 0], p=[self.p_in_neg, 1 - self.p_in_neg])
                else:
                    positive_weight_matrix[i][j] = np.random.choice([1, 0], p=[self.p_out_pos, 1 - self.p_out_pos])
                    negative_weight_matrix[i][j] = np.random.choice([1, 0], p=[self.p_out_neg, 1 - self.p_out_neg])

                positive_weight_matrix[j][i] = positive_weight_matrix[i][j]
                negative_weight_matrix[j][i] = negative_weight_matrix[i][j]

        return positive_weight_matrix, negative_weight_matrix
