// React Theme — extracted from https://www.busybeehoney.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '14': string;
    '15': string;
    '16': string;
    '24': string;
    '65': string;
    '185': string;
    '210': string;
    '112.667': string;
    '76.6667': string;
    '25.3333': string;
    '18.6667': string;
    '15.3333': string;
 *   };
 *   space: {
    '6': string;
    '60': string;
    '80': string;
    '218': string;
 *   };
 *   radii: {
    full: string;
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
    "primary": "#ffca50",
    "secondary": "#3b2722",
    "accent": "#a0342a",
    "background": "#f2ebd0",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#6fa162"
  },
  "fonts": {
    "body": "'AnonymousPro-Regular', sans-serif"
  },
  "fontSizes": {
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "24": "24px",
    "65": "65px",
    "185": "185px",
    "210": "210px",
    "112.667": "112.667px",
    "76.6667": "76.6667px",
    "25.3333": "25.3333px",
    "18.6667": "18.6667px",
    "15.3333": "15.3333px"
  },
  "space": {
    "6": "6px",
    "60": "60px",
    "80": "80px",
    "218": "218px"
  },
  "radii": {
    "full": "1000px"
  },
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
    "primary": {
      "main": "#ffca50",
      "light": "hsl(42, 100%, 81%)",
      "dark": "hsl(42, 100%, 51%)"
    },
    "secondary": {
      "main": "#3b2722",
      "light": "hsl(12, 27%, 33%)",
      "dark": "hsl(12, 27%, 10%)"
    },
    "background": {
      "default": "#f2ebd0",
      "paper": "#ffca50"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#3b2722"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "65px",
      "fontWeight": "400",
      "lineHeight": "65px"
    },
    "h2": {
      "fontSize": "25.3333px",
      "fontWeight": "400",
      "lineHeight": "25.3333px"
    }
  },
  "shape": {
    "borderRadius": 38
  },
  "shadows": []
};

export default theme;
