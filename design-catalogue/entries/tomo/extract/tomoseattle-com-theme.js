// React Theme — extracted from https://tomoseattle.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '28': string;
    '28.8': string;
    '23.04': string;
    '13.3333': string;
    '11.52': string;
 *   };
 *   space: {
    '1': string;
    '58': string;
    '99': string;
    '116': string;
    '143': string;
    '269': string;
    '293': string;
    '338': string;
    '360': string;
    '369': string;
    '415': string;
    '474': string;
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
    "primary": "#ff6347",
    "secondary": "#eee2d4",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#f0f0f0",
    "neutral300": "#1a1a1a"
  },
  "fonts": {
    "body": "'Arial', sans-serif"
  },
  "fontSizes": {
    "28": "28px",
    "28.8": "28.8px",
    "23.04": "23.04px",
    "13.3333": "13.3333px",
    "11.52": "11.52px"
  },
  "space": {
    "1": "1px",
    "58": "58px",
    "99": "99px",
    "116": "116px",
    "143": "143px",
    "269": "269px",
    "293": "293px",
    "338": "338px",
    "360": "360px",
    "369": "369px",
    "415": "415px",
    "474": "474px"
  },
  "radii": {
    "full": "100px"
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
      "main": "#ff6347",
      "light": "hsl(9, 100%, 79%)",
      "dark": "hsl(9, 100%, 49%)"
    },
    "secondary": {
      "main": "#eee2d4",
      "light": "hsl(32, 43%, 95%)",
      "dark": "hsl(32, 43%, 73%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#ff6347"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h2": {
      "fontSize": "28px",
      "fontWeight": "400",
      "lineHeight": "28px"
    },
    "h3": {
      "fontSize": "23.04px",
      "fontWeight": "400",
      "lineHeight": "23.04px"
    },
    "body2": {
      "fontSize": "11.52px",
      "fontWeight": "400",
      "lineHeight": "normal"
    }
  },
  "shape": {
    "borderRadius": 100
  },
  "shadows": []
};

export default theme;
