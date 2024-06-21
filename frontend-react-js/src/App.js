import './App.css';

import HomeFeedPage from './pages/HomeFeedPage';
import NotificationsFeedPage from './pages/NotificationsFeedPage';
import UserFeedPage from './pages/UserFeedPage';
import SignupPage from './pages/SignupPage';
import SigninPage from './pages/SigninPage';
import RecoverPage from './pages/RecoverPage';
import MessageGroupsPage from './pages/MessageGroupsPage';
import MessageGroupPage from './pages/MessageGroupPage';
import ConfirmationPage from './pages/ConfirmationPage';
import React from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { Amplify } from 'aws-amplify';

// Ensure that all required environment variables are available
const {
  REACT_APP_AWS_PROJECT_REGION,
  REACT_APP_AWS_COGNITO_REGION,
  REACT_APP_AWS_USER_POOLS_ID,
  REACT_APP_CLIENT_ID,
} = process.env;

Amplify.configure({
  Auth: {
    region: REACT_APP_AWS_PROJECT_REGION,
    userPoolId: REACT_APP_AWS_USER_POOLS_ID,
    userPoolWebClientId: REACT_APP_CLIENT_ID,
  },
  oauth: {},
});

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomeFeedPage />,
  },
  {
    path: "/notifications",
    element: <NotificationsFeedPage />,
  },
  {
    path: "/@:handle",
    element: <UserFeedPage />,
  },
  {
    path: "/messages",
    element: <MessageGroupsPage />,
  },
  {
    path: "/messages/@:handle",
    element: <MessageGroupPage />,
  },
  {
    path: "/signup",
    element: <SignupPage />,
  },
  {
    path: "/signin",
    element: <SigninPage />,
  },
  {
    path: "/confirm",
    element: <ConfirmationPage />,
  },
  {
    path: "/forgot",
    element: <RecoverPage />,
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
