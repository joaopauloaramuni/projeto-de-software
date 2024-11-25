public class Main {
    public static void main(String[] args) {
        // Usando DAO diretamente
        UserDAO userDAO = new UserDAOImpl();
        User user = new User();
        user.setName("Alice");
        userDAO.save(user);

        // Usando Repository
        UserRepository userRepository = new UserRepositoryImpl();
        userRepository.addUser(user);
    }
}