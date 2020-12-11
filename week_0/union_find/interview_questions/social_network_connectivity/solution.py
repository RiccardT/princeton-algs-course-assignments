from week_0.union_find.interview_questions.social_network_connectivity.FacebookFriendConnector import \
    FacebookFriendConnector
from test_utilities.dynamic_test_creator import \
    run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.social_network_connectivity_functionality_test_data import \
    social_network_connectivity_functionality_test_data


def earliest_network_was_connected_fully(connections: list, friends: int) -> int:  # O(m*log(n))
    """
    1. connect m[i].friend_1 with m[i].friend_2
    2. update max_tree_size variable which keeps track of the largest tree in the graph
    3. if max_tree_size() equals n, then return m[0].time, else continue looping through m.

    this algorithm takes m iterations at worst with log(n) work in each iteration, therefore O(m*log(n))
    """
    facebook_connector = FacebookFriendConnector(friends)
    for connection in connections:  # O(m)
        facebook_connector.union(connection.friend_1, connection.friend_2)  # O(log(n)
        if facebook_connector.all_connected():  # O(1)
            return connection.time_of_connection
    return -1


if __name__ == '__main__':
    dynamically_generate_tests(social_network_connectivity_functionality_test_data,
                               earliest_network_was_connected_fully,
                               timed=True)
    run_dynamic_tests()
