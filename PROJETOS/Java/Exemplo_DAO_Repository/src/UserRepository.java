public interface UserRepository {
    void addUser(User user);
    User getUser(int id);
    void updateUser(User user);
    void removeUser(int id);
}
