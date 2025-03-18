// Preducer.js
import { ADD_CART, REMOVE_ITEM } from './actionTypes';

const initialState = {
  cartItems: [],
};

const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_CART:
      const existingItemIndex = state.cartItems.findIndex(item => item.id === action.payload.id);
      if (existingItemIndex >= 0) {
        // Item already exists in the cart, update the quantity
        const updatedCartItems = [...state.cartItems];
        updatedCartItems[existingItemIndex].quantity += action.payload.quantity;
        return {
          ...state,
          cartItems: updatedCartItems,
        };
      } else {
        // Item does not exist, add it to the cart
        return {
          ...state,
          cartItems: [...state.cartItems, { ...action.payload, quantity: 1 }], // Default quantity to 1
        };
      }

    case REMOVE_ITEM:
      return {
        ...state,
        cartItems: state.cartItems.filter(item => item.id !== action.payload),
      };

    default:
      return state;
  }
};

export default cartReducer;