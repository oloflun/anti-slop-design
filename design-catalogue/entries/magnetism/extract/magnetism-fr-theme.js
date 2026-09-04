// React Theme — extracted from https://magnetism.fr
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '6': string;
    '24': string;
    '21.3334': string;
    '17.7778': string;
    '14.2222': string;
    '12.4444': string;
    '9.77779': string;
    '8.88889': string;
    '8.88883': string;
    '7.11117': string;
 *   };
 *   space: {
    '4': string;
    '43': string;
    '50': string;
    '57': string;
    '71': string;
    '89': string;
    '114': string;
    '124': string;
    '136': string;
    '160': string;
    '382': string;
 *   };
 *   radii: {

 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "background": "#343434",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#222222",
    "neutral200": "#000000",
    "neutral300": "#343434",
    "neutral400": "#aaaaaa",
    "neutral500": "#dbdbdb",
    "neutral600": "#cccccc"
  },
  "fonts": {
    "body": "'NeueMontreal', sans-serif"
  },
  "fontSizes": {
    "6": "6px",
    "24": "24px",
    "21.3334": "21.3334px",
    "17.7778": "17.7778px",
    "14.2222": "14.2222px",
    "12.4444": "12.4444px",
    "9.77779": "9.77779px",
    "8.88889": "8.88889px",
    "8.88883": "8.88883px",
    "7.11117": "7.11117px"
  },
  "space": {
    "4": "4px",
    "43": "43px",
    "50": "50px",
    "57": "57px",
    "71": "71px",
    "89": "89px",
    "114": "114px",
    "124": "124px",
    "136": "136px",
    "160": "160px",
    "382": "382px"
  },
  "radii": {},
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "background": {
      "default": "#343434",
      "paper": "#ececec"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#222222"
    }
  },
  "typography": {
    "fontFamily": "'NeueMontreal', sans-serif",
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "24px"
    },
    "h3": {
      "fontSize": "21.3334px",
      "fontWeight": "400",
      "lineHeight": "32.0001px"
    },
    "body1": {
      "fontSize": "17.7778px",
      "fontWeight": "400",
      "lineHeight": "26.6667px"
    },
    "body2": {
      "fontSize": "9.77779px",
      "fontWeight": "400",
      "lineHeight": "14.6667px"
    }
  },
  "shape": {},
  "shadows": []
};

export default theme;
